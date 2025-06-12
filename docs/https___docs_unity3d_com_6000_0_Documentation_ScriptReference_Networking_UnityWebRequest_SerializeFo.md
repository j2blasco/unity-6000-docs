* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SerializeFormSections.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).SerializeFormSections
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
public static byte[] SerializeFormSections(List<IMultipartFormSection> multipartFormSections, byte[] boundary); 
### Parameters
Parameter | Description  
---|---  
multipartFormSections | A List of [IMultipartFormSection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.IMultipartFormSection.html) objects.  
boundary | A unique boundary string to separate the form sections.  
### Returns
**byte[]** A byte array of raw multipart form data. 
### Description
Converts a List of IMultipartFormSection objects into a byte array containing raw multipart form data.
Additional resources: [GenerateBoundary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GenerateBoundary.html).
* * *
