* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.GetInactiveOptions.html

#  [ToggleButtonGroupState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.html).GetInactiveOptions
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
public Span<int> GetInactiveOptions(Span<int> inactiveOptionsIndices); 
### Parameters
Parameter | Description  
---|---  
inactiveOptionsIndices | A Span of type integers with the allocated size to hold the number of inactive indices.  
### Description
Retrieves a Span of integers containing the inactive options as indices. 
```
 public void HandleInactiveOptions()
 {
     var value = myToggleButtonGroup.value;
     var options = value.GetInactiveOptions(stackalloc int[value.length]);
     foreach (option in options)
     {
         // handle option
     }
 }

```

* * *
