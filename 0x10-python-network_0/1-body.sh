#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
res= $(curl -sL -w "%{http_code}" "$1"); stat=$(echo "$res"|cut -d" " -f2); if ["$stat" -eq 200] then; rsult= $(echo "$res" | cut -d" " f1); fi; echo"$result"
