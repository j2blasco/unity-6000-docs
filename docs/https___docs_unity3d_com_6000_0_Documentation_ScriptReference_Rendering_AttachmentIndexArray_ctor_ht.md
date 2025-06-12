* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray-ctor.html

# AttachmentIndexArray Constructor
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
public AttachmentIndexArray(int numAttachments); 
## Declaration
public AttachmentIndexArray(int[] attachments); 
## Declaration
public AttachmentIndexArray(NativeArray<int> attachments); 
### Parameters
Parameter | Description  
---|---  
numAttachments | Number of indices to allocate.  
attachments | Allocate and copy the passed-in list of indices.  
### Description
Create and initialize a new AttachmentIndexArray.
Individual items can be read/writen using the indexer operator.
* * *
