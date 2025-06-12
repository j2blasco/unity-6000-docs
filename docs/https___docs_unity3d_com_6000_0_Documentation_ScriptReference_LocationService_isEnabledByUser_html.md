* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService-isEnabledByUser.html

#  [LocationService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService.html).isEnabledByUser
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
isEnabledByUser; 
### Description
Indicates whether the device allows the application to access the location service.
Check this property before you start location updates to determine if the device has location services enabled and that the application has access to them.  
  
**Android** : The property returns false if the application has no permission to access location. If you start the location service updates, the user receives location permission request (unless already granted or permanently denied). Before starting the location service updates, you can query to check whether the application has location permission.  
  
**iOS** : The property returns false if the application has no permission to access location. If you start the location updates anyway, the device prompts the user with a confirmation panel asking whether to enable location services for the application. For more information, refer to [Apple's developer documentation](https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled\(\)?language=objc).  
  
**WebGL** : The property is false until you start location updates. Once location updates start, it reflects the permissions granted by the user in the browser.
* * *
