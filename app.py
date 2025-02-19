
import streamlit as st
import random

# Title
st.title("🌱 Growth Mindset Challenge")
st.write("Develop your skills through persistence and learning!")

# List of 50 challenges
challenges = [
    "Reflect on a past mistake and what you learned from it.",
    "Try a new learning technique and note how it helps.",
    "Identify a challenge you're currently facing and outline a plan to overcome it.",
    "Help someone else learn something new today.",
    "Write about a time when you overcame self-doubt.",
    "Learn one new word today and use it in a sentence.",
    "Find a quote that inspires you and reflect on its meaning.",
    "Identify a bad habit and take the first step to break it.",
    "Make a list of three things you are grateful for today.",
    "Practice active listening in your next conversation.",
    "Write about a goal you've been avoiding and commit to starting it today.",
    "Ask someone for feedback on your work and implement one suggestion.",
    "Challenge yourself to step out of your comfort zone today.",
    "Read a short article on a topic you know little about.",
    "Set a small goal for today and achieve it.",
    "Think of a skill you want to improve and take action on it.",
    "Reframe a negative thought into a positive one.",
    "Spend 5 minutes meditating or doing deep breathing.",
    "Learn a productivity tip and apply it today.",
    "Identify a mistake you've made and write down how you can improve.",
    "Celebrate a small win today, no matter how small.",
    "Practice giving yourself positive affirmations.",
    "Write down one thing you’re proud of achieving this year.",
    "Try a different problem-solving approach to a challenge.",
    "Spend time teaching someone a skill you have mastered.",
    "Reflect on how failure has helped you grow.",
    "Ask someone about their biggest challenge and how they overcame it.",
    "Try something new that you've been hesitant about.",
    "Spend time journaling about a difficult experience and what it taught you.",
    "Identify an area of personal growth and take action to improve it.",
    "Make a plan to overcome a fear you've been avoiding.",
    "Find a mentor or role model and learn about their journey.",
    "Turn a complaint into a solution-focused action step.",
    "Take responsibility for a past mistake and learn from it.",
    "Spend time appreciating how far you have come in life.",
    "Learn about a successful person's failures and how they overcame them.",
    "Practice perseverance in an activity that challenges you.",
    "Replace self-criticism with self-encouragement today.",
    "Write down three qualities you admire in yourself.",
    "Challenge yourself to do something you’ve never done before.",
    "Be patient with yourself while learning something difficult.",
    "Break a big goal into small steps and take the first step today.",
    "Find one way to improve your focus and apply it today.",
    "Create a plan to develop a skill you want to master.",
    "Share something inspiring with a friend today.",
    "Think about a person who inspires you and why.",
    "Try a new problem-solving strategy at work or school.",
    "List three ways you have shown resilience in the past.",
    "Give yourself permission to be imperfect and keep learning.",
    "Spend time visualizing your ideal future self and take action toward it."
]

# List of 50 motivational quotes
quotes = [
    "“Success is not final, failure is not fatal: it is the courage to continue that counts.” – Winston Churchill",
    "“Do not be embarrassed by your failures, learn from them and start again.” – Richard Branson",
    "“It does not matter how slowly you go as long as you do not stop.” – Confucius",
    "“Failure is simply the opportunity to begin again, this time more intelligently.” – Henry Ford",
    "“Believe you can and you’re halfway there.” – Theodore Roosevelt",
    "“Your only limit is your mind.” – Unknown",
    "“If you are not willing to risk the usual, you will have to settle for the ordinary.” – Jim Rohn",
    "“Hardships often prepare ordinary people for an extraordinary destiny.” – C.S. Lewis",
    "“If you learn from defeat, you haven’t really lost.” – Zig Ziglar",
    "“Don’t limit your challenges, challenge your limits.” – Jerry Dunn",
    "“Growth and comfort do not coexist.” – Ginni Rometty",
    "“The best way to predict the future is to create it.” – Peter Drucker",
    "“Never let success get to your head and never let failure get to your heart.” – Drake",
    "“Success is getting what you want. Happiness is wanting what you get.” – Dale Carnegie",
    "“Do what you can, with what you have, where you are.” – Theodore Roosevelt",
    "“You are confined only by the walls you build yourself.” – Andrew Murphy",
    "“Success is stumbling from failure to failure with no loss of enthusiasm.” – Winston Churchill",
    "“You don’t have to be great to start, but you have to start to be great.” – Zig Ziglar",
    "“Work hard in silence, let your success be your noise.” – Frank Ocean",
    "“Every expert was once a beginner.” – Helen Hayes",
    "“Failure is the tuition you pay for success.” – Walter Brunell",
    "“Your attitude determines your direction.” – Unknown",
    "“You don’t have to see the whole staircase, just take the first step.” – Martin Luther King Jr.",
    "“Every strike brings me closer to the next home run.” – Babe Ruth",
    "“Everything you’ve ever wanted is on the other side of fear.” – George Addair",
    "“Small progress is still progress.” – Unknown",
    "“You miss 100% of the shots you don’t take.” – Wayne Gretzky",
    "“Act as if what you do makes a difference. It does.” – William James",
    "“Dream big and dare to fail.” – Norman Vaughan",
    "“A river cuts through rock, not because of its power, but because of its persistence.” – Jim Watkins",
    "“Doubt kills more dreams than failure ever will.” – Suzy Kassem",
    "“Nothing will work unless you do.” – Maya Angelou",
    "“The harder you work for something, the greater you’ll feel when you achieve it.” – Unknown",
    "“Success is the sum of small efforts repeated day in and day out.” – Robert Collier",
    "“Discipline is the bridge between goals and accomplishment.” – Jim Rohn",
    "“Opportunities don’t happen, you create them.” – Chris Grosser",
    "“Your limitation—it’s only your imagination.” – Unknown",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Live as if you were to die tomorrow. Learn as if you were to live forever.” – Mahatma Gandhi",
    "“Action is the foundational key to all success.” – Pablo Picasso",
    "“Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.” – Roy T. Bennett",
    "“If you want to achieve greatness, stop asking for permission.” – Unknown",
    "“Always do your best. What you plant now, you will harvest later.” – Og Mandino"
]

# Challenge selection
if st.button("🔄 Get Today's Challenge"):
    st.subheader("✨ Your Challenge for Today:")
    st.write(random.choice(challenges))

# Motivational quote selection
if st.button("💡 Get a Motivational Quote"):
    st.subheader("🌟 Inspiration for Today:")
    st.write(random.choice(quotes))
