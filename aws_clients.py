import boto3
from config import AWS_CREDENTIALS_PATH, DEFAULT_REGION
from botocore.config import Config
import configparser

class AwsClientManager:
    def __init__(self):
        self.account_id_rds_clients = {}
        self.account_id_secrets_manager_clients = {}
        self.account_id_cloudwatch_clients = {}
        self.account_id_pi_clients = {}

        self.init_aws_clients()
        print('rds',self.account_id_rds_clients)
    def init_aws_clients(self):
        config = configparser.ConfigParser()
        config.read(AWS_CREDENTIALS_PATH)

        for profile_name in config.sections():
            session = boto3.Session(profile_name=profile_name)
            account_id = self.get_aws_account_id(session)

            self.account_id_rds_clients[account_id] = session.client('rds', region_name=DEFAULT_REGION)
            self.account_id_secrets_manager_clients[account_id] = session.client('secretsmanager', region_name=DEFAULT_REGION)
            self.account_id_cloudwatch_clients[account_id] = session.client('cloudwatch', region_name=DEFAULT_REGION)
            self.account_id_pi_clients[account_id] = session.client('pi', region_name=DEFAULT_REGION)

    def get_aws_account_id(self, session):
        sts_client = session.client('sts', config=Config(region_name=DEFAULT_REGION))
        return sts_client.get_caller_identity().get('Account')

    def get_rds_client(self, account_id):
        return self.account_id_rds_clients.get(account_id)

    def get_secrets_manager_client(self, account_id):
        return self.account_id_secrets_manager_clients.get(account_id)

    def get_cloudwatch_client(self, account_id):
        return self.account_id_cloudwatch_clients.get(account_id)

    def get_pi_client(self, account_id):
        return self.account_id_pi_clients.get(account_id)

    def find_all_rds_clients(self):
        return self.account_id_rds_clients

    def find_all_secrets_manager_clients(self):
        return self.account_id_secrets_manager_clients

    def find_all_cloudwatch_clients(self):
        return self.account_id_cloudwatch_clients

    def find_all_pi_clients(self):
        return self.account_id_pi_clients

if __name__ == "__main__":
    manager = AwsClientManager()
    print(manager.find_all_rds_clients())
    rds_clients=manager.find_all_rds_clients()
    for account_id in rds_clients:
        print(account_id)
        rds_client=rds_clients[account_id]
        a=manager.get_rds_client(account_id)
        print('a',a)
        print('a',a.describe_db_clusters())
    print(rds_client)
    print(rds_client.describe_db_clusters())
    