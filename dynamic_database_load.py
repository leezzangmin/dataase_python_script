import boto3


def find_all_cluster_info():
    rds_client = boto3.client('rds', region_name='ap-northeast-2')
    response = rds_client.describe_db_clusters()
    print(response)
    pass


    # public Map<String, List<DBCluster>> findAllClusterInfo() {
    #     Map<String, List<DBCluster>> dbClusters = new HashMap<>();

    #     Map<String, RdsClient> rdsClients = awsClient.findAllRdsClients();
    #     for (String accountId : rdsClients.keySet()) {
    #         RdsClient rdsClient = rdsClients.get(accountId);
    #         DescribeDbClustersResponse describeDbClustersResponse = rdsClient.describeDBClusters();
    #         DescribeDbClustersResponse clustersResponse = findValidClusters(describeDbClustersResponse);
    #         List<DBCluster> accountClusters = clustersResponse.dbClusters();
    #         dbClusters.put(accountId, accountClusters);
    #     }

    #     log.info("clusters: {}", dbClusters);
    #     return dbClusters;
    # }
print(1)