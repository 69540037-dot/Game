Python
import streamlit as st
import random

# 1. ลิสต์คำศัพท์ทั้งหมดของเรา
vocab = [
    ["cucumber", "แตงกวา"],
    ["Lion", "สิงโต"],
    ["Snake", "งู"],
    ["Vegetable", "ผัก"],
    ["River", "แม่น้ำ"],
    ["Iron", "เหล็ก"],
    ["Headphone", "หูฟัง"],
    ["Bottle", "ขวด"],
    ["Nail", "เล็บ"],
    ["Rice", "ข้าว"]
]

# 2. ตั้งค่าตัวแปรเริ่มต้น (Session State)
if "started" not in st.session_state:
    st.session_state.started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_vocab" not in st.session_state:
    st.session_state.game_vocab = []
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🎮 เกมทายคำศัพท์ภาษาอังกฤษ")

# 3. หน้าแรก: ตอนผู้เล่นกดเริ่มเกม (เอาชุดโค้ดใหม่ไปใส่ตรงนี้!)
if not st.session_state.started:
    st.subheader("พร้อมจะลุยกันหรือยัง?")
    col1, col2 = st.columns(2)
    
    with col1:
        # --- ใส่โค้ดสับไพ่ตรงนี้เลยครับ! ---
        if st.button("กด 1: ลุยเลย! 🚀"):
            st.session_state.started = True
            
            # สับคำศัพท์แบบไม่ให้ซ้ำกันเก็บไว้ก่อนเริ่มเล่น
            shuffled_vocab = vocab.copy()
            random.shuffle(shuffled_vocab)
            st.session_state.game_vocab = shuffled_vocab
            
            st.session_state.current_question = 1
            st.session_state.score = 0
            st.session_state.game_over = False
            st.rerun()
            
    with col2:
        if st.button("กด 0: ไม่เล่น ออกเกม 👋"):
            st.warning("กำลังออกจากเกม... ไว้ว่างๆ มาเล่นกันใหม่นะ!")

# 4. หน้าเล่นเกม: ดึงคำศัพท์จากตัวแปร game_vocab ที่สับแล้วมาแสดงทีละข้อ
elif st.session_state.started and not st.session_state.game_over:
    q_idx = st.session_state.current_question - 1 # ดึงตามลำดับข้อ 0 ถึง 9
    current_word = st.session_state.game_vocab[q_idx]
    
    english_word = current_word[0]
    thai_word = current_word[1]
    
    st.subheader(f"ข้อที่ {st.session_state.current_question}/10")
    st.markdown(f"### คำว่า **'{english_word}'** แปลว่าอะไร?")
    
    user_answer = st.text_input("พิมพ์คำตอบของคุณที่นี่:", key=f"q_{st.session_state.current_question}")
    
    if st.button("ส่งคำตอบ 🎯"):
        if user_answer.strip() == thai_word:
            st.success("ถูกต้อง! เก่งมาก! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"ผิดดด! คำตอบที่ถูกต้องคือ '{thai_word}' 😅")
            
        if st.session_state.current_question < 10:
            st.session_state.current_question += 1
            st.button("ไปข้อถัดไป ➡️")
        else:
            st.session_state.game_over = True
            st.rerun()

# 5. หน้าจบเกม
else:
    st.balloons()
    st.header(f"🏁 จบเกมแล้ว! คุณได้คะแนนทั้งหมด {st.session_state.score}/10 คะแนน")
    
    if st.button("เล่นใหม่อีกครั้ง 🔄"):
        st.session_state.started = False
        st.rerun()
