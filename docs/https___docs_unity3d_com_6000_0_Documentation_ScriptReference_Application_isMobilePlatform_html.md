* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isMobilePlatform.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).isMobilePlatform
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
isMobilePlatform; 
### Description
Identifies whether the current Runtime platform is a known mobile platform.
Currently this returns true if the application is running on Android, iOS, or WSA. When targeting WebAssembly and running in a web browser, this property might return "true" or "false", depending on whether the current browser is running on a mobile device. Due to privacy and anonymization reasons, this property might not always report accurate information on all web browsers.  
  
**Note** : On Universal Windows Platform, tablets are treated as desktop machines, therefore, this property returns true only when running on phones and IoT device family devices.
* * *
