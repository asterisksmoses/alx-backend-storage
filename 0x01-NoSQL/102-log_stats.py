#!/usr/bin/env python3

"""This module provides some stats about Nginx logs
stored in MonogDB."""

from pymongo import MongoClient

def nginx_stats():
    """This function prints some stats about nginx logs
    stored in MongoDB."""

    client = MongoClient('mongodb://localhost:27017/')
    db = clinet.logs
    nginx_collection = db.nginx

    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    print("IPs:")
    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
    ]

    top_ips = list(nginx_collection.aggregate(pipeline))
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    pass
