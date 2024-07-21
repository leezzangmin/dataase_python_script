import boto3
import aws_clients

def find_all_cluster_info():
    manager = aws_clients.AwsClientManager()
    
    rds_clients = manager.find_all_rds_clients()
    for account_id in rds_clients:
        rds_client = rds_clients[account_id]
        describe_db_clusters_response = rds_client.describe_db_clusters()
        print(describe_db_clusters_response)
        for i in describe_db_clusters_response:
            print(i)
            print(type(i),'ttttt')
        print('tpe',type(describe_db_clusters_response))



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

def isValidDbCluster(describe_db_clusters_response):
    # describe_db_clusters_response.
    pass

    #     private DescribeDbClustersResponse findValidClusters(DescribeDbClustersResponse describeDbClustersResponse) {
    #     DescribeDbClustersResponse clustersResponse = DescribeDbClustersResponse.builder()
    #             .dbClusters(describeDbClustersResponse.dbClusters().stream()
    #                     .filter(cluster -> cluster.status().equals("available"))
    #                     .filter(cluster -> !cluster.tagList().contains(TagStandard.standardTagKeyNames))
    #                     .filter(cluster -> isCurrentEnvHasValidTag(cluster.tagList()))
    #                     .collect(Collectors.toList()))
    #             .build();
    #     return clustersResponse;
    # }
    

find_all_cluster_info()
