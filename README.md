# Analyse-DZ ⚽🇩🇿
### منصة التحليل التكتيكي الرياضي الاحترافي لمباريات كرة القدم
**تطوير وتأسيس: الكابتن بن عبدالله الهواري (مربي رياضي، محلل أداء، ومدرب حراس مرمى)**

---

## 🚀 المميزات الرئيسية
- **استوديو التحليل التكتيكي المتعدد الزوايا (Multi-Angle Video Studio)**
- **تقطيع الفيديو ومقاطع المباريات بدقة عالية**
- **مصفوفة التكويد الفوري (Event Tagging Matrix)**
- **أدوات الرسم والتوضيح الفني والتراكب التكتيكي (Tactical Overlay & Freehand Drawing)**
- **الخريطة الحرارية المتقدمة (Tactical Heatmap)** لتحركات اللاعبين وتوزيع الكثافة التكتيكية
- **مقارنة الفيديو المزدوجة (Dual Video Comparison)**
- **تصدير التقارير الفنية بصيغ متعددة (PDF / JSON / CSV)**
- **دعم تطبيق الويب التقدمي (PWA)** للتثبيت المباشر على الهاتف والحاسوب

---

## 🛠 التشغيل محلياً (Local Development)

```bash
# تثبيت الحزم والمكتبات
npm install

# تشغيل خادم التطوير
npm run dev
```

التطبيق سيعمل على: `http://localhost:3000`

---

## 🌐 النشر والرفع على Vercel و GitHub

### 1. الرفع على GitHub:
```bash
git init
git add .
git commit -m "Initial commit of Analyse-DZ platform"
git branch -M main
git remote add origin https://github.com/USERNAME/analyse-dz.git
git push -u origin main
```

### 2. الرفع على Vercel:
1. توجه إلى [vercel.com](https://vercel.com) وسجّل الدخول بحساب GitHub.
2. اضغط على **"Add New..."** ثم **"Project"**.
3. اختر مستودع `analyse-dz` من قائمتك في GitHub.
4. الإعدادات جاهزة تلقائياً بفضل ملف `vercel.json` المرفق في المشروع (Framework Preset: Vite, Build: `npm run build`, Output: `dist`).
5. اضغط **"Deploy"**! في أقل من دقيقة سيصبح تطبيقك منشوراً برابط عالمي مجاني فائق السرعة مع شهادة SSL.
