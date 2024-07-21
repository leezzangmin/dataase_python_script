import aws_clients

if __name__ == "__main__":
    manager = aws_clients.AwsClientManager()
    print(manager.find_all_rds_clients())
    rds_clients=manager.find_all_rds_clients()
    for account_id in rds_clients:
        print(account_id)
        rds_client=rds_clients[account_id]
        
    print(rds_client)
    print(rds_client.describe_db_clusters())
    