from jupextdemo.azaks_deploy import *
from jupextdemo.gitHubManager import GithubManager
def _test_accounts():
    pass


def deployMain():
    
    # this will run in the initial load , for now we assume user has cluster and acr account. we pick up the first account in that case. 
    # replyObject = {};
    # aks_dep = AKSDeploy();
    # if aks_dep.IsUserLoggedIn() :
    #     replyObject["DefaultSubscription"] = aks_dep.getDefaultSubscription()
    # else:
    #     aks_dep.loginUserFlow()
    #     replyObject["DefaultSubscription"] = aks_dep.getDefaultSubscription() 

    # # get ACR details
    # replyObject["ACRAccount"] = aks_dep.getACRDetails()

    # # get AKS details
    # replyObject["AKSCluster"] =  aks_dep.getAKSDetails()
    
    # this reply object will go to the JS which will store it in the cookie for now

    # this should run after user press the deploy button
    # now use this object and pass it to Github manager from JS when user presses deploy

    gm = GithubManager("ec121ac9f7f39a927968d2ffcdf11ec7a3054f12")
    gm.getRepo();
    gm.commitAppFile();
    # akscluster = replyObject["AKSCluster"][0] if len(replyObject["AKSCluster"])> 0 else None;
    # acrAccount = replyObject["ACRAccount"][0] if len(replyObject["ACRAccount"])> 0 else None;
    # gm.pushDeployFilestoRepo(akscluster,acrAccount)
        
if __name__ == "__main__":
    deployMain()