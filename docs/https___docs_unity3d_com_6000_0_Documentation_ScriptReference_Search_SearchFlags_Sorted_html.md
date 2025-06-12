* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Sorted.html

#  [SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html).Sorted
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
Fetched items are sorted by the search service.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

public class SearchFlags_Sorted
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html)/Sorted")]
    public static void RequestAll()
    {
        ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results = SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)("p: t:Script", SearchFlags.Sorted[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Sorted.html));
        AsyncResultEnumerator.Fetch(results, item => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(item));
    }

    struct AsyncResultEnumerator
    {
        private Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> m_OnEnumerate;
        private IEnumerator<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> m_Iterator;
        private ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) m_SearchList;

        public static AsyncResultEnumerator Fetch(ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> onEnumerate)
        {
            return new AsyncResultEnumerator(results, onEnumerate);
        }

        public AsyncResultEnumerator(ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> onEnumerate)
        {
            m_OnEnumerate = onEnumerate;
            m_SearchList = results;
            m_Iterator = results.GetEnumerator();
            EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) += WaitForSearchCompleted;
        }

        private void WaitForSearchCompleted()
        {
            // Wait for the search to complete, otherwise it will not yield sorted items.
            if (!m_SearchList.pending)
            {
                EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) -= WaitForSearchCompleted;
                EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) += EnumerateResults;
            }
        }

        private void EnumerateResults()
        {
            if (m_Iterator == null || !m_Iterator.MoveNext())
            {
                m_Iterator = null;
                EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) -= EnumerateResults;
            }
            else if (m_Iterator.Current != null)
                m_OnEnumerate(m_Iterator.Current);
        }
    }
}

```

* * *
