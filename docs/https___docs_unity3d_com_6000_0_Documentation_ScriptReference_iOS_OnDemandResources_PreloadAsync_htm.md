* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResources.PreloadAsync.html

#  [OnDemandResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResources.html).PreloadAsync
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
public static [iOS.OnDemandResourcesRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html) PreloadAsync(string[] tags); 
### Parameters
Parameter | Description  
---|---  
tags | Tags for On Demand Resources that should be included in the request.  
### Returns
**OnDemandResourcesRequest** Object representing ODR request. 
### Description
Creates an On Demand Resources (ODR) request.
The request will include all resources indicated by the given tags. If operation completes successfuly, then the request object will keep those resources alive until [OnDemandResourcesRequest.Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.Dispose.html) is called or the request gets collected by a garbage collector.  
  
Additional resources: [OnDemandResourcesRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html).
* * *
