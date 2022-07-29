docker run -it --rm \
  -v /Users/beer/beer/go_fleet/gopacket_demo:/Users/beer/beer/go_fleet/gopacket_demo \
  -w /Users/beer/beer/go_fleet/gopacket_demo \
  -e CGO_ENABLED=1 \
  -e GOPROXY="https://goproxy.cn,direct" \
  beer5215/golang-crossbuild-debian10 \
  --build-cmd "go build" \
  -p "windows/amd64"