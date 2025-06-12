* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState-ctor.html

# ToggleButtonGroupState Constructor
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
public ToggleButtonGroupState(ulong optionsBitMask, int length); 
### Parameters
Parameter | Description  
---|---  
optionsBitMask | A bit value where each bit represents the binary state of the corresponding button.  
length | The number of toggle button options.  
### Description
Constructs a ToggleButtonGroupState. 
The maximum number of toggle button options allowed is 64. Exceeding this number will throw an ArgumentOutOfRangeException. 
* * *
