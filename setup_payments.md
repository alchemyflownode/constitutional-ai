## 💳 Setup Real Payments:

### Option A: Stripe (Recommended)
1. Go to: stripe.com
2. Create "Buy Now" button for $49
3. Get link: https://buy.stripe.com/test_xxx
4. Replace button onclick in HTML

### Option B: Gumroad (Easier)
1. Go to: gumroad.com
2. Create product "Constitutional AI"
3. Price: $49
4. Upload zip file
5. Use Gumroad's checkout link

### In HTML, replace:
<button onclick="showPurchaseModal()">...</button>

### With:
<a href="YOUR_STRIPE_LINK" class="...">BUY NOW</a>
