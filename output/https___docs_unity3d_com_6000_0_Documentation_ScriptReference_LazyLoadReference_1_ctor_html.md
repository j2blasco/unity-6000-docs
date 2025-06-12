* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-ctor.html

# LazyLoadReference<T0> Constructor
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
public LazyLoadReference<T0>(T asset); 
## Declaration
public LazyLoadReference<T0>(int instanceID); 
### Parameters
Parameter | Description  
---|---  
asset | The asset reference.  
instanceID | The asset instance ID.  
### Description
Construct a new LazyLoadReference.
Note that the signature which takes an asset reference may trigger loading the referenced object into memory if the object is not already loaded. The signature which takes an instance ID will never triggers a load.
* * *
