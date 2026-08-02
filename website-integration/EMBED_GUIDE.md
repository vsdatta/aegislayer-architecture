# Embed and Link Guide

## Preferred Integration

Use external links from website pages to canonical technical docs and demo artifacts.

## Optional Demo Embedding

Embed the demo via iframe only where policy allows:

```html
<iframe
  title="AegisLayer interactive demo"
  src="https://vsdatta.github.io/aegislayer-architecture/demo/"
  loading="lazy"
  style="width: 100%; min-height: 720px; border: 0;"
></iframe>
```

## Accessibility Note

Provide a direct link fallback for browsers that block iframes.
