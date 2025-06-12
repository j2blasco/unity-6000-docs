* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetTreeInstance.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).GetTreeInstance
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
public [TreeInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeInstance.html) GetTreeInstance(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the tree instance.  
### Description
Gets the tree instance at the specified index. It is used as a faster version of [treeInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-treeInstances.html)[index] as this function doesn't create the entire tree instances array.
* * *
