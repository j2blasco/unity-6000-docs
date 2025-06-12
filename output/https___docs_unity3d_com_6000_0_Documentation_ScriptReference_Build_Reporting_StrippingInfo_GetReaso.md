* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.StrippingInfo.GetReasonsForIncluding.html

#  [StrippingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.StrippingInfo.html).GetReasonsForIncluding
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
public IEnumerable<string> GetReasonsForIncluding(string entityName); 
### Parameters
Parameter | Description  
---|---  
entityName | The name of an engine module, class, or other entity present in the build.  
### Returns
**IEnumerable <string>** A list of modules, classes, or other entities that caused the provided entity to be included in the build. 
### Description
Returns the list of dependencies or reasons that caused the given entity to be included in the build.
The returned list of strings may include names of components, internal engine objects, other modules, or other human-readable reasons. To obtain further information, you can pass each string back into GetReasonsForIncluding again.  
  
For example, calling GetReasonsForIncluding("Physics Module") may return a list that includes "Rigidbody", and you can then call GetReasonsForIncluding("Rigidbody") to get more information about which Scenes or assets are using the Rigidbody component.
* * *
