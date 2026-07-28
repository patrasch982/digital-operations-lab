#!/bin/bash

echo "======================================"
echo " Digital Operations Lab - Status"
echo "======================================"
echo

echo "Hostname:"
hostname

echo
echo "Uptime:"
uptime -p

echo
echo "Speicher:"
free -h

echo
echo "Festplatte:"
df -h /

echo
echo "Docker Container:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo
echo "Docker Netzwerk:"
docker network ls
