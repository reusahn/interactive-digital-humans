import { useEffect, useState } from 'react'
import { ArrowDown, ArrowUpRight, ChevronRight, CircleDot, Menu, Network, Pause, Play, Radio, Sparkles, X } from 'lucide-react'

const pillars = [
  { no: '01', title: 'REPRESENT', ko: '표현하다', text: 'Neural fields that capture identity, motion, and appearance as a coherent, editable 4D signal.', tags: ['Gaussian Avatars', 'Dynamic NeRF', 'Parametric Bodies'], color: '#dfff3f' },
  { no: '02', title: 'GENERATE', ko: '생성하다', text: 'World-aware generative models that synthesize photoreal humans, motion, and behavior on demand.', tags: ['Diffusion', 'Motion Synthesis', 'Neural Rendering'], color: '#8b7dff' },
  { no: '03', title: 'EMBODY', ko: '체화하다', text: 'Responsive agents that perceive, reason, and act naturally within shared physical and virtual space.', tags: ['Embodied Agents', 'Social Intelligence', 'Real-time Control'], color: '#ff704d' },
]

const metrics = [
  ['28', 'MS', 'PHOTON-TO-MOTION'], ['120', 'FPS', 'NEURAL RENDERING'], ['360°', '', 'FREE-VIEWPOINT'], ['∞', '', 'GENERATIVE MOTION'],
]

function HumanFigure({ playing }) {
  return <div className={`figure-wrap ${playing ? 'playing' : ''}`} aria-label="Animated point-cloud digital human visualization">
    <div className="scan-ring ring-a"/><div className="scan-ring ring-b"/><div className="ground-ring"/>
    <div className="human">
      <div className="head"><i/><i/><i/></div><div className="neck"/><div className="torso"><span/><span/><span/></div>
      <div className="arm left"><span/><span/></div><div className="arm right"><span/><span/></div>
      <div className="leg left"><span/><span/></div><div className="leg right"><span/><span/></div>
    </div>
    <div className="point-field">{Array.from({length: 42}, (_, i) => <i key={i} style={{'--x': `${(i * 47) % 100}%`, '--y': `${(i * 73) % 100}%`, '--d': `${(i % 7) * -.3}s`}} />)}</div>
    <div className="axis-label label-a">GAZE VECTOR <b>0.92</b></div><div className="axis-label label-b">SKELETON <b>TRACKING</b></div>
  </div>
}

export default function App() {
  const [playing, setPlaying] = useState(true)
  const [menu, setMenu] = useState(false)
  const [active, setActive] = useState(0)
  const [time, setTime] = useState('00:00:00')
  useEffect(() => { const started = Date.now(); const id = setInterval(() => { const sec = Math.floor((Date.now()-started)/1000); setTime(`00:${String(Math.floor(sec/60)).padStart(2,'0')}:${String(sec%60).padStart(2,'0')}`) },1000); return () => clearInterval(id)}, [])

  return <main>
    <nav>
      <a className="brand" href="#top"><span>K</span>KINETICA<small>4D HUMAN INTELLIGENCE</small></a>
      <div className={`navlinks ${menu ? 'open' : ''}`}>
        <a href="#research" onClick={()=>setMenu(false)}>RESEARCH</a><a href="#framework" onClick={()=>setMenu(false)}>FRAMEWORK</a><a href="#manifesto" onClick={()=>setMenu(false)}>MANIFESTO</a>
        <button className="access" onClick={()=>document.getElementById('research').scrollIntoView({behavior:'smooth'})}>ENTER THE LAB <ArrowUpRight size={15}/></button>
      </div>
      <button className="menu" onClick={()=>setMenu(!menu)} aria-label="Toggle navigation">{menu ? <X/> : <Menu/>}</button>
    </nav>

    <section className="hero" id="top">
      <div className="hero-grid"/><div className="side-code">KINETICA / SYSTEM 04 — 2026</div>
      <div className="eyebrow"><span className="pulse"/> RESEARCH INITIATIVE · SEOUL / GLOBAL</div>
      <h1>BUILDING<br/><em>HUMANS</em><br/>BEYOND<br/><strong>FRAMES.</strong></h1>
      <p className="lede">AI-driven digital humans that <b>see, think, move,</b> and <b>interact</b> — continuously, naturally, and in real time.</p>
      <a href="#research" className="scroll"><ArrowDown size={15}/> EXPLORE THE RESEARCH</a>
      <div className="visual-panel"><HumanFigure playing={playing}/>
        <div className="panel-top"><span><CircleDot size={12}/> LIVE INFERENCE</span><b>{time}</b></div>
        <button className="play" onClick={()=>setPlaying(!playing)} aria-label={playing ? 'Pause simulation' : 'Play simulation'}>{playing ? <Pause size={17}/> : <Play size={17}/>}</button>
        <div className="panel-bottom"><span>SUBJECT <b>DH_0042</b></span><span>LATENCY <b>28MS</b></span><span>CONFIDENCE <b>98.7%</b></span></div>
      </div>
    </section>

    <section className="statement" id="manifesto"><div className="kicker">THE RESEARCH QUESTION</div><h2>HOW DO WE GIVE<br/>DIGITAL HUMANS<br/><em>A SENSE OF NOW?</em></h2><p>Not just avatars that look human.<br/>Intelligences that inhabit time and space.</p></section>

    <section className="pillars" id="research">
      <div className="section-head"><div><span>RESEARCH PILLARS</span><h2>FROM CAPTURE<br/>TO <em>PRESENCE.</em></h2></div><p>Three interconnected research tracks form a unified stack for truly interactive digital life.</p></div>
      <div className="pillar-list">{pillars.map((p,i)=><article key={p.no} className={active===i?'active':''} onMouseEnter={()=>setActive(i)} style={{'--accent':p.color}}>
        <header><span>{p.no}</span><Network size={24}/></header><div className="orb"><span/></div><h3>{p.title}<small>{p.ko}</small></h3><p>{p.text}</p><div className="tags">{p.tags.map(t=><span key={t}>{t}</span>)}</div><button onClick={()=>setActive(i)}>EXPLORE TRACK <ChevronRight size={15}/></button>
      </article>)}</div>
    </section>

    <section className="framework" id="framework">
      <div className="framework-copy"><span className="green-label"><Sparkles size={14}/> UNIFIED FRAMEWORK</span><h2>ONE HUMAN.<br/>EVERY <em>DIMENSION.</em></h2><p>Our systems close the loop between perception and action—maintaining identity, physical plausibility, and social context across every frame.</p><a href="#pipeline">VIEW SYSTEM ARCHITECTURE <ArrowUpRight size={15}/></a></div>
      <div className="pipeline" id="pipeline"><div className="flow-line"/>{['PERCEIVE','UNDERSTAND','GENERATE','ACT'].map((x,i)=><div className="flow" key={x}><span>0{i+1}</span><div><i>{i===0?<Radio/>:i===1?<CircleDot/>:i===2?<Sparkles/>:<Network/>}</i></div><b>{x}</b><small>{['Multi-modal sensing','World modeling','Motion + appearance','Real-time embodiment'][i]}</small></div>)}</div>
    </section>

    <section className="numbers"><div className="number-intro"><span>DESIGNED FOR<br/>THE SPEED OF<br/><em>INTERACTION.</em></span></div>{metrics.map(m=><div className="metric" key={m[2]}><strong>{m[0]}</strong><b>{m[1]}</b><span>{m[2]}</span></div>)}</section>
    <footer><a className="brand" href="#top"><span>K</span>KINETICA</a><p>RESEARCHING THE NEXT INTERFACE<br/>BETWEEN HUMAN AND MACHINE.</p><div><a href="mailto:lab@kinetica.research">LAB@KINETICA.RESEARCH</a><span>© 2026 KINETICA LAB</span></div></footer>
  </main>
}
