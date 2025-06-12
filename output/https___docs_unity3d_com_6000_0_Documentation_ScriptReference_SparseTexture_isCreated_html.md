* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture-isCreated.html

#  [SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html).isCreated
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
isCreated; 
### Description
Is the sparse texture actually created? (Read Only)
Sparse texture contents can become "lost", mostly on graphics device change or active color space switch. When that happens, isCreated will start returning false - meaning you should recreate all the needed tiles again.  
  
Additional resources: [SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html).
* * *
