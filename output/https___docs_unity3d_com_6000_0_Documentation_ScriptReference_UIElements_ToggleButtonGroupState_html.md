* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.html

# ToggleButtonGroupState
struct in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
### Description
The structure that keeps track of the [Button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) states inside a [ToggleButtonGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroup.html). 
To set properties on how to serialize this type, use [ToggleButtonGroupStatePropertiesAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupStatePropertiesAttribute.html). 
### Properties
Property | Description  
---|---  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState-length.html) |  Returns the number of toggle button options available.   
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.Index_operator.html) |  The option based on the index.   
### Constructors
Constructor | Description  
---|---  
[ToggleButtonGroupState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState-ctor.html) |  Constructs a ToggleButtonGroupState.   
### Public Methods
Method | Description  
---|---  
[CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.CompareTo.html) |  Compares two ToggleButtonGroupState.   
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.Equals.html) |  Checks if a given ToggleButtonGroupState matches with the current one.   
[GetActiveOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.GetActiveOptions.html) |  Retrieves a Span of integers containing the active options as indices.   
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.GetHashCode.html) |  Get the hashcode of this ToggleButtonGroupState.   
[GetInactiveOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.GetInactiveOptions.html) |  Retrieves a Span of integers containing the inactive options as indices.   
[ResetAllOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.ResetAllOptions.html) |  Resets the states of the toggle buttons.   
[SetAllOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.SetAllOptions.html) |  Sets all the available options to active.   
[ToggleAllOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.ToggleAllOptions.html) |  Toggles all the available options' state.   
### Static Methods
Method | Description  
---|---  
[Compare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.Compare.html) |  Compares two ToggleButtonGroupState of flag enum types.   
[CreateFromOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.CreateFromOptions.html) |  Helps generate a ToggleButtonGroupState based on a list of booleans.   
[FromEnumFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.FromEnumFlags.html) |  Creates a ToggleButtonGroupState based on a FlagsAttribute enum type.   
[ToEnumFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.ToEnumFlags.html) |  Synchronizes the internal data with the ToggleButtonGroupState from a FlagsAttribute.   
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState-operator_ne.html) |  Checks if both of the ToggleButtonGroupState are not the same.   
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState-operator_eq.html) |  Checks if both of the ToggleButtonGroupState are the same.   
* * *
