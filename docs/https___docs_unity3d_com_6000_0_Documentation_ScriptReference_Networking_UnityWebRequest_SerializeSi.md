* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SerializeSimpleForm.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).SerializeSimpleForm
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
public static byte[] SerializeSimpleForm(Dictionary<string,string> formFields); 
### Parameters
Parameter | Description  
---|---  
formFields | A dictionary containing the form keys and values to serialize.  
### Returns
**byte[]** A byte array containing the serialized form. The form's keys and values have been URL-encoded. 
### Description
Serialize a dictionary of strings into a byte array containing URL-encoded UTF8 characters.
This method will URL-encode the strings, then concatenate them as if they were in an HTTP query string. Keys and values will be separated with an equals sign (=) and different key-value pairs will be separated with ampersands (&).
* * *
