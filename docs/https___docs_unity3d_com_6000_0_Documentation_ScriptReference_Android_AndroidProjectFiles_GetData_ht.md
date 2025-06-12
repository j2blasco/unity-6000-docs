* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.GetData.html

#  [AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html).GetData
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
public string GetData(string key); 
### Parameters
Parameter | Description  
---|---  
key | Data key.  
value | Data value as string.  
### Description
Gets data that was set in the Setup method.
This method is used to get data from the Unity Editor by setting it in the `Setup` method.  
  
If data with the the given key does not exist, Unity throws an error.
* * *
## Declaration
public T GetData(string key); 
### Parameters
Parameter | Description  
---|---  
key | Data key.  
value | Serializable object.  
### Description
Gets data that was set in the Setup method.
This method is used to get data from the Unity Editor by setting it in the `Setup` method.  
  
If data with the the given key does not exist, Unity throws an error.
* * *
