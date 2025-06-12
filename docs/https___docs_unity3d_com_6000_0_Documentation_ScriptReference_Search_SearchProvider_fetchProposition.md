* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchPropositions.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).fetchPropositions
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
fetchPropositions; 
### Description
Handler used to enumerate search propositions when the user is using TAB to auto-complete a query.
```
IEnumerable<SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)> FetchPropositions(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchPropositionOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionOptions.html) options)
{
  foreach (var f in myFilters)
    yield return new SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)(f.name, f.name, f.label);
}
```

* * *
