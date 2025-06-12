* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.ForEach.html

#  [UQueryState<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.html).ForEach
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
public void ForEach(Action<T> funcCall); 
### Parameters
Parameter | Description  
---|---  
funcCall | The action to be invoked with each matching element.  
### Description
Invokes function on all elements matching the query. 
* * *
## Declaration
public void ForEach(List<T2> result, Func<T,T2> funcCall); 
### Parameters
Parameter | Description  
---|---  
result | Each return value will be added to this list.  
funcCall | The function to be invoked with each matching element.  
### Description
Invokes function on all elements matching the query. 
* * *
## Declaration
public List<T2> ForEach(Func<T,T2> funcCall); 
### Parameters
Parameter | Description  
---|---  
funcCall | The action to be invoked with each matching element.  
### Description
Invokes function on all elements matching the query. 
* * *
