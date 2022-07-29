package main

import (
	"fmt"
	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
	"github.com/google/gopacket/pcap"
	"log"
	"strings"
)

// FindAllDevs 获取所有 ip
func FindAllDevs() {
	devices, _ := pcap.FindAllDevs()
	for _, device := range devices {
		for _, address := range device.Addresses {
			if len(address.IP) == 0 {
				continue
			}
			if strings.Contains(address.IP.String(), ":") {
				continue
			}
			if strings.HasPrefix(address.IP.String(), "127") {
				continue
			}
			fmt.Printf("\nName: [%s], IP address: [%s] ", device.Name, address.IP.String())
		}
	}
}

func OpenLive() {
	handle, err := pcap.OpenLive("eth0", 1000, false, 5)
	if err != nil {
		log.Fatal(err)
	}
	defer handle.Close()
	// Use the handle as a packet source to process all packets
	packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
	for packet := range packetSource.Packets() {
		// Process packet here
		fmt.Println(packet)
	}
}

func DecodePacket() {
	var myPacketData []byte //todo

	// Decode a packet
	packet := gopacket.NewPacket(myPacketData, layers.LayerTypeEthernet, gopacket.Default)
	// Get the TCP layer from this packet
	if tcpLayer := packet.Layer(layers.LayerTypeTCP); tcpLayer != nil {
		fmt.Println("This is a TCP packet!")
		// Get actual TCP data from this layer
		tcp, _ := tcpLayer.(*layers.TCP)
		fmt.Printf("From src port %d to dst port %d\n", tcp.SrcPort, tcp.DstPort)
	}
	// Iterate over all layers, printing out each layer type
	for _, layer := range packet.Layers() {
		fmt.Println("PACKET LAYER:", layer.LayerType())
	}
}

func main() {
	FindAllDevs()
	//OpenLive()
}
