# -*- coding: utf-8 -*-

api_list = [{
    "id": "time",
    "name": "Time",
    "desc": "Get now time.",
    "method": "GET",
    "url": "http://vps.jack003.com/api/v1.0/time",
    "parameters": None,
    "example_response": '{"status": "success", "data": "Thu, 02 Feb 2016 15:31:28 GMT"}'
}, {
    "id": "jalpc-count",
    "name": "Jalpc Count",
    "desc": "Get Jalpc website PV count.",
    "method": "GET, JSONP",
    "url": "http://vps.jack003.com/api/v1.0/jalpc/pv_count",
    "parameters": None,
    "example_response": '{"status": "success", "data": 186768}'
}, {
    "id": "rss-reader",
    "name": "RSS",
    "desc": "Get website's rss content.",
    "method": "GET, JSONP",
    "url": "http://vps.jack003.com/api/v1.0/rss",
    "parameters": "url",
    "example_response": '{"msg": "success", "data": "xxxxxxx"}'
}, {
    "id": "request-info",
    "name": "Request/IP Infomation",
    "desc": "Get request/IP information, no parameter is localhost.",
    "method": "GET",
    "url": "http://vps.jack003.com/api/v1.0/info",
    "parameters": "ip",
    "example_response": '{"data": {"ip": "127.0.0.1", "ip_information": "{"cityName": ...}", "user_agent": {"browser": "chrome",<br> "language": null, "platform": "macos", "string": "Mozilla/5.0 (Macintosh...", "version": "55.0.2883.95"}},<br> "status": "success"}'
}]
