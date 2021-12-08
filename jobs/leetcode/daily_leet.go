package leetcode

import (
	"github.com/tidwall/gjson"
	"job/utils"
	"strings"
)

func GetDailyUrl() string {
	baseUrl := "https://leetcode-cn.com/problems/"
	var data = strings.NewReader(`{
	"query": "\n    query questionOfToday {\n  todayRecord {\n    date\n    userStatus\n    question {\n      questionId\n      frontendQuestionId: questionFrontendId\n      difficulty\n      title\n      titleCn: translatedTitle\n      titleSlug\n      paidOnly: isPaidOnly\n      freqBar\n      isFavor\n      acRate\n      status\n      solutionNum\n      hasVideoSolution\n      topicTags {\n        name\n        nameTranslated: translatedName\n        id\n      }\n      extra {\n        topCompanyTags {\n          imgUrl\n          slug\n          numSubscribed\n        }\n      }\n    }\n    lastSubmission {\n      id\n    }\n  }\n}\n    ",
	"variables": {},
	"operationName": "questionOfToday"
}`)
	headers := make(map[string]string)
	headers["content-type"] = "application/json"
	headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
	bodyText := utils.HttpPost("https://leetcode-cn.com/graphql", data, headers)
	if bodyText != "" {
		titleSlug := gjson.Get(string(bodyText), "data.todayRecord.0.question.titleSlug").String()
		return baseUrl + titleSlug
	}
	return ""
}
