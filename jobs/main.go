package main

import (
	"fmt"
	"github.com/tidwall/gjson"
	"job/leetcode"
	"job/utils"
	"os"
	"time"
)

func GetParam() utils.WeixinConf {
	text := utils.ReadJsonFile("/opt/wechat.json")
	if text == "" {
		os.Exit(-1)
	}
	conf := new(utils.WeixinConf)
	conf.Corpsecret = gjson.Get(text, "corpsecret").String()
	conf.Corpid = gjson.Get(text, "corpid").String()
	conf.Agentid = gjson.Get(text, "agentid").String()
	conf.Touser = gjson.Get(text, "touser").String()
	return *conf
}

func main() {
	dailyUrl := leetcode.GetDailyUrl()
	nowDate := time.Now().Format("2006-01-02")

	//send text
	text := fmt.Sprintf(`Date: %s \nLeetcode: %s`, nowDate, dailyUrl)

	result := utils.SendText(text, GetParam())
	fmt.Print(result)
}
