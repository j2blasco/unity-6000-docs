* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.AdvertisingIdentifierCallback.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).AdvertisingIdentifierCallback
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
public delegate void AdvertisingIdentifierCallback(string advertisingId, bool trackingEnabled, string errorMsg); 
### Parameters
Parameter | Description  
---|---  
advertisingId | Advertising ID.  
trackingEnabled | Indicates whether the user has chosen to limit ad track.  
errorMsg | Error message.  
### Description
Delegate method for fetching advertising ID.
Additional resources:[Application.RequestAdvertisingIdentifierAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestAdvertisingIdentifierAsync.html)
* * *
