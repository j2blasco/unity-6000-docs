* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-serializeInlineMappingsOnOneLine.html

#  [EditorSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings.html).serializeInlineMappingsOnOneLine
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
serializeInlineMappingsOnOneLine; 
### Description
Forces Unity to write references and similar YAML structures on one line, which reduces version control noise.
When Unity reaches a line length of 80 characters it attempts to split the [YAML](https://docs.unity3d.com/6000.0/Documentation/Manual/FormatDescription.html) data over multiple lines. To avoid unwanted version control changes, this setting forces Unity to ignore the 80 character check. Note: The Project Setting menu refers to this setting as **Reduce version control noise**.  
  
**Without setting**  
`m_MySerializedAssetReference: {fileID: 10304, guid: a2eb3ee376dd24a4f9221a30765d895b,`  
`type: 3}`  
  
**With setting**  
`m_MySerializedAssetReference: {fileID: 10304, guid: a2eb3ee376dd24a4f9221a30765d895b, type: 3}`
* * *
