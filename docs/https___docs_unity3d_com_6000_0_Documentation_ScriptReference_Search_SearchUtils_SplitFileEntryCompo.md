* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SplitFileEntryComponents.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).SplitFileEntryComponents
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
public static IEnumerable<string> SplitFileEntryComponents(string path, ref char[] entrySeparators); 
### Parameters
Parameter | Description  
---|---  
path | Path to tokenize.  
entrySeparators | Entry separators used to tokenize the path.  
### Returns
**IEnumerable <string>** Returns list of tokens and variations in lowercase. 
### Description
Split a file entry according to a list of separators and find all the variations on the entry name.
* * *
