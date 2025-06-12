* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# ArtifactKey
struct in UnityEditor.Experimental
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
### Description
An ArtifactKey is used for specifying an artifact to lookup or produce.
One example of producing an artifact is to run and importer on a specific asset. The importer is specified by type (e.g. typeof(MyImporter) and the asset by its guid. From these two you can create an ArtifactKey and use it to ask the assetdatabase to produce the artifact. You can also create an ArtifactKey from only a guid. In that case the AssetDatabase will automatically select the importer from the list of valid importers.
### Properties
Property | Description  
---|---  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey-guid.html) | The guid specifying the asset in question.  
[importerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey-importerType.html) | The managed type of the importer to use for producing the artifact.  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey-isValid.html) | Returns true is the hash value is valid. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[ArtifactKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey-ctor.html) | Construct an ArtifactKey.  
* * *
