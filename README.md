# To Software — game privacy and deletion

Shared public privacy policy and account/data deletion request pages for To Software casual and arcade games that link to them, including Rainbow Jump and Color Collision.

| Language | Privacy | Deletion request |
| --- | --- | --- |
| pt-BR | https://tosoftwarestudio.github.io/rainbow-jump-privacy/ | https://tosoftwarestudio.github.io/rainbow-jump-privacy/exclusao-de-dados/ |
| en-US | https://tosoftwarestudio.github.io/rainbow-jump-privacy/en/ | https://tosoftwarestudio.github.io/rainbow-jump-privacy/en/delete-data/ |
| es | https://tosoftwarestudio.github.io/rainbow-jump-privacy/es/ | https://tosoftwarestudio.github.io/rainbow-jump-privacy/es/eliminar-datos/ |

Public responsible/support name: **To Software**. Contact: **tosoftwarestudio@gmail.com**.

The legacy repository/URL name is retained so existing store/app links keep working. Naming a game in the policy does not assert that it is released or that every optional feature is active. Disclosures depend on the actual title/version, enabled services and included SDKs.

## Maintenance

Edit the three files in `content/`, then run `python3 tools/build_site.py`. Commit sources and generated HTML together. GitHub Pages serves static files from the `main` branch root with `.nojekyll`; there is no application server, analytics script, login, age questionnaire or server-side deletion form.

Before adding a materially different title, service, SDK, purchase or analytics feature, update the actual data inventory and all three translations. Each game's Play Data safety declarations still require inspection of that game's build; this common policy is not a universal answer sheet.

## Deletion operations

The site opens an email request. It does not automatically erase accounts. The operator must monitor the public inbox, identify the requested game(s), verify ownership proportionately without asking for passwords/tokens, delete applicable Authentication/Leaderboards/other associated records, verify the result, and reply with the outcome and any justified retention. Do not delete another game's profile unless the request covers it. Guest ownership may need additional verification; a public display name alone is insufficient.

In-app links, CMP integration, privacy/age settings, backend erasure and native acceptance remain each game's responsibility. The intended audience is 13+; an age questionnaire is not part of these shared pages.

## Primary maintenance references

- Google Play User Data: https://support.google.com/googleplay/android-developer/answer/10144311?hl=en
- Account deletion: https://support.google.com/googleplay/android-developer/answer/13327111?hl=en
- Google Mobile Ads disclosures: https://developers.google.com/admob/android/privacy/play-data-disclosure
- Unity Ads disclosures (match each game's installed version): https://docs.unity.com/en-us/ads-android/4.21.0/privacy/developer-consent/disclosures/google-data-safety
- LevelPlay/ironSource disclosures: https://docs.unity.com/en-us/grow/is-ads/legal-resources/google-data-safety-questionnaire
