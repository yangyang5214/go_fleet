package utils

import (
	"fmt"
	"io/ioutil"
	"os"
)

func ReadJsonFile(path string) string {
	jsonFile, err := os.Open(path)
	if err != nil {
		fmt.Println(err)
		return ""
	}
	defer jsonFile.Close()
	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		fmt.Println(err)
		return ""
	}
	return string(byteValue)
}
