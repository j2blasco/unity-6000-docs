* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.Property_2.Accept.html

#  [Property<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.Property_2.html).Accept
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
public void Accept([Unity.Properties.IPropertyVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyVisitor.html) visitor, ref TContainer container); 
### Parameters
Parameter | Description  
---|---  
visitor | The visitor being run.  
container | The container being visited.  
### Description
Call this method to invoke IPropertyVisitor.Visit_2 with the strongly typed container and value. 
* * *
