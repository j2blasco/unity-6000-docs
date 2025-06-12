* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DecodeSelectionId.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).DecodeSelectionId
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
public static int DecodeSelectionId([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) selectionId); 
### Parameters
Parameter | Description  
---|---  
selectionId | The selection ID retrieved from GPU to translate into a picking index.  
### Returns
**int** The decoded picking index. 
### Description
Translates a Vector4 `selectionId` value retrieved from GPU into a single integer picking index.
Additional resources: [HandleUtility.EncodeSelectionId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.EncodeSelectionId.html).
* * *
