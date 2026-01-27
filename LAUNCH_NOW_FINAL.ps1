Write-Host "🚀 LAUNCH EXECUTION SCRIPT" -ForegroundColor Cyan
Write-Host "1. Opening all launch files..." -ForegroundColor Yellow

# Open all necessary files
Start-Process notepad "QUICK_PAYMENT_SETUP.md"
Start-Process notepad "SOCIAL_MEDIA_POSTS.md"
Start-Process notepad "LAUNCH_CHECKLIST.md"

Write-Host "`n2. Launch URLs to copy:" -ForegroundColor Yellow
Write-Host "   Hacker News: https://news.ycombinator.com/submit" -ForegroundColor White  
Write-Host "   Reddit: https://www.reddit.com/r/selfhosted/submit" -ForegroundColor White
Write-Host "   Twitter: https://twitter.com/compose/tweet" -ForegroundColor White        
Write-Host "   LinkedIn: https://www.linkedin.com/shareArticle" -ForegroundColor White

# ⚠️ REPLACE THESE WITH YOUR ACTUAL URLs ⚠️
$ProductURL = "https://your-actual-demo-url.com"
$PaymentURL = "https://buy.stripe.com/your-actual-link"

Write-Host "`n3. Your product URL: $ProductURL" -ForegroundColor Green   
Write-Host "4. Your payment URL: $PaymentURL" -ForegroundColor Green   

Write-Host "`n📋 Copy this launch post:" -ForegroundColor Yellow
Write-Host "---" -ForegroundColor Gray
Write-Host "Built Constitutional AI because I was tired of cloud dependencies and wanted actual guardrails for my AI projects." -ForegroundColor White
Write-Host ""
Write-Host "Demo: $ProductURL" -ForegroundColor White
Write-Host "GitHub: [YOUR_GITHUB_URL]" -ForegroundColor White
Write-Host ""
Write-Host "Key features:" -ForegroundColor White
Write-Host "• Local AI governance with constitutional AI principles" -ForegroundColor Gray
Write-Host "• No cloud dependencies - runs entirely locally" -ForegroundColor Gray
Write-Host "• Built-in safety guardrails for AI projects" -ForegroundColor Gray
Write-Host "• Supports 15+ Ollama models out of the box" -ForegroundColor Gray
Write-Host "---" -ForegroundColor Gray

Write-Host "`n🎯 GO LAUNCH! Post this NOW!" -ForegroundColor Magenta
