# 💰 QUICK PAYMENT SETUP (15 minutes)

## Option A: Stripe (Recommended - 10 min)
1. Go to: https://dashboard.stripe.com/register
2. Create account with your email
3. Click "Products" → "Add Product"
4. Name: "Constitutional AI"
5. Price: $49.00
6. Click "Create product"
7. Copy "Buy now" link
8. Update HTML: Replace onclick="showPurchaseModal()" with href="YOUR_STRIPE_LINK"

## Option B: Gumroad (Easiest - 5 min)
1. Go to: https://gumroad.com
2. Sign up
3. Click "Add new product"
4. Name: "Constitutional AI"
5. Price: $49
6. Upload: Constitutional_AI_Package.zip
7. Click "Create"
8. Use Gumroad's checkout link

## HTML Update:
Replace:
<button onclick="showPurchaseModal()">BUY NOW</button>

With:
<a href="YOUR_PAYMENT_LINK" class="buy-btn">BUY NOW</a>

## Test Purchase:
1. Use test card: 4242 4242 4242 4242
2. Any future date, any CVC
3. Should show success immediately

## You're Ready to Sell! 🚀
