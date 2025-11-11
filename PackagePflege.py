from tts.core.api.internalApi.Api import Api

api = Api()
import os


obj = api.ObjectApi
wk = obj.WorkspaceApi
pkg = obj.PackageApi
       
#Search all testcases that have used pkg, and then modify them in batches
def Replace_Parameter_Value(PkgPath, PkgParameters, OldValue, NewValue):
    
    
    
    
    path_of_Package = str(PkgPath[0])
    index = path_of_Package.rfind('\\')
    PackageName = path_of_Package[index + 1: -4]
   
    #Parameters = 'variableToRead'
    Parameters = PkgParameters
    
    #New_Configured_Value = "'Kaswhis_Test'"
    New_Configured_Value = "'" + NewValue + "'"
    
    #Old_Configured_Value = "'Cr_S_HoistSpeedGapCoeff'"
    Old_Configured_Value = "'" + OldValue + "'"
    
    
    
    
    Reference_of_Pkg = []
    
    #Search all testcases that have used pkg,return a list of path
    Reference_of_Pkg = wk.GetReferencesTo(path_of_Package)
    
    
    for element in Reference_of_Pkg:
    
        openPkg = pkg.OpenPackage(element)
        
        
        for TS in openPkg.GetTestSteps(skipDisabledSteps=True, recursive=True, whiteList=None, blackList=None):
            
            if TS.GetType() == 'TsPackage':
                Name = TS.GetAbsolutePath()
                indexName = Name.rfind('\\')
                TsPackageName = Name[index + 1 : -4]
                Parameter_TestStep = TS.GetPackageParameters()
                
                if TsPackageName == PackageName: 
                
                    if Parameters in Parameter_TestStep and Parameter_TestStep[Parameters] == Old_Configured_Value:
                    
                        #replace the configured value  
                        TS.SetPackageParameter(Parameters, New_Configured_Value)
                        Line = TS.GetLineNo()
                        
                        
        openPkg.Save(element)
        openPkg.Close()
                
                
               
                     
    return 
    
# Search Package which with predefined paramter and value. tTen print the linenumber, related package und related packagepath into a txtfile.        
def SearchPkgReferences(txtFolder, PkgPath, PkgParameters, ParameterValue):
 
    txtFolder_Path = txtFolder
    
    
    pkgPath = str(PkgPath[0])
    
    index = pkgPath.rfind('\\')
    PackageName = pkgPath[index + 1: -4]
    txtName = pkgPath[index + 1: -4] + '_References' + '.txt'
    txtFilePath = 'r' + "'" + txtFolder_Path + "'"
    filepath = os.path.join(txtFolder, txtName)
    Parameters = PkgParameters
   
    Configured_Value = "'" + ParameterValue + "'"
    
    
    with open(filepath, 'w') as file:
        Reference_of_Pkg = []
        Reference_of_Pkg = wk.GetReferencesTo(pkgPath)
        
        for element in Reference_of_Pkg:
        
            openPkg = pkg.OpenPackage(element)
            indexPkgPath = element.rfind('\\')
            PkgName = element[indexPkgPath + 1: ]
            
           
            for TS in openPkg.GetTestSteps(skipDisabledSteps=True, recursive=True, whiteList=None, blackList=None):
                  
                if TS.GetType() == 'TsPackage':
                        Name = TS.GetAbsolutePath()
                        indexName = Name.rfind('\\')
                        TsPackageName = Name[index + 1 : -4]
                        Parameter_TestStep = TS.GetPackageParameters()
                        if TsPackageName == PackageName: 
                            Line = TS.GetLineNo()
                            if Parameters != '' and Configured_Value != '':  
                                if Parameters in Parameter_TestStep and Parameter_TestStep[Parameters] == Configured_Value: 
                                    
                                    file.write(str(Line) + '        ' + str(PkgName) + '          ' + str(element) + '\n')    
                
                            else:
                                
                                file.write(str(Line) + '        ' + str(PkgName) + '          ' + str(element) + '\n')
            
            openPkg.Close()
            
                
               
                
                
                    
    
    return
    
        

        
        
    
        