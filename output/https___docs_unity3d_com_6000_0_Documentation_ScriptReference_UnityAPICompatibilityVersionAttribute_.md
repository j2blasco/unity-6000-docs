* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityAPICompatibilityVersionAttribute-ctor.html

# UnityAPICompatibilityVersionAttribute Constructor
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public UnityAPICompatibilityVersionAttribute(string version, bool checkOnlyUnityVersion); 
### Parameters
Parameter | Description  
---|---  
version | Unity version that this assembly is compatible with.  
checkOnlyUnityVersion | Must be set to true.  
### Description
Initializes a new instance of UnityAPICompatibilityVersionAttribute.
Use this overload during the development cycle to avoid the AssemblyUpdater check that is performed on game code built outside of Unity and imported as assemblies. You can also avoid this check by passing disable-assembly-updater as a command line argument (see the Unity Manual for more details).
* * *
**Obsolete** This overload of the attribute has been deprecated. Use the constructor that takes the version and a boolean.
## Declaration
public UnityAPICompatibilityVersionAttribute(string version); 
### Parameters
Parameter | Description  
---|---  
version | Unity version that this assembly is compatible with.  
### Description
Initializes a new instance of UnityAPICompatibilityVersionAttribute. This overload has been deprecated.
* * *
## Declaration
public UnityAPICompatibilityVersionAttribute(string version, string[] configurationAssembliesHashes); 
### Parameters
Parameter | Description  
---|---  
version | Unity version that this assembly is compatible with.  
configurationAssembliesHashes | A comma-separated list comprised of the assembly name and attribute hash pairs. For example, assemblyname:hash,assemblyname:hash.  
### Description
Initializes a new instance of UnityAPICompatibilityVersionAttribute. This constructor is used by internal tooling.
* * *
