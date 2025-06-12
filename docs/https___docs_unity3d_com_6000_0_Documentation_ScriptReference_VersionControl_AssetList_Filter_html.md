* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.Filter.html

#  [AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html).Filter
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
public [VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) Filter(bool includeFolder, params States[] states); 
### Parameters
Parameter | Description  
---|---  
includeFolder | Whether or not folders should be included.  
states | Which states to filter by.  
### Description
Based on the current list and the states a new list is returned which only contains the assets with the requested states.
* * *
