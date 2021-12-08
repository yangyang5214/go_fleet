package utils

import (
	"fmt"
	"github.com/tidwall/gjson"
	"strings"
)

type WeixinConf struct {
	Corpid     string
	Corpsecret string
	Touser     string
	Agentid    string
}

func getAccessToken(conf WeixinConf) string {
	params := make(map[string]string)
	params["corpid"] = conf.Corpid
	params["corpsecret"] = conf.Corpsecret
	respText := HttpGet("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params, nil)
	if respText != "" {
		return gjson.Get(respText, "access_token").String()
	}
	return ""
}

func SendText(content string, conf WeixinConf) string {
	accessToken := getAccessToken(conf)
	touser := conf.Touser
	agentid := conf.Agentid
	body := fmt.Sprintf(`{
		"touser": "%s",
		"agentid": "%s",
		"msgtype": "text",
		"text": {
			"content": "%s"
		}
	}`, touser, agentid, content)
	return HttpPost("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+accessToken, strings.NewReader(body), nil)
}
