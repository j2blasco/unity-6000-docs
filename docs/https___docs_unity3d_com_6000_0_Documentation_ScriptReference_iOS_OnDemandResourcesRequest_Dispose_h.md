* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.Dispose.html

#  [OnDemandResourcesRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html).Dispose
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
public void Dispose(); 
### Description
Release all resources kept alive by On Demand Resources (ODR) request.
[OnDemandResourcesRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html) will keep the on demand resource alive until either [Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.Dispose.html) is called or the request object is collected by the garbage collector, which is the equivalent of calling [NSBundleResourceRequest.endAccessingResources](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSBundleResourceRequest_Class/) class.
* * *
