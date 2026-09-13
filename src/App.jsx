import { useEffect, useState } from 'react'
import {
  ArrowDown,
  ArrowUpRight,
  ChevronRight,
  CircleDot,
  Menu,
  Network,
  Pause,
  Play,
  Radio,
  Sparkles,
  X,
} from 'lucide-react'

const pillars = [
  {
    no: '01',
    title: 'REPRESENT',
    ko: '표현하다',
    text: 'Real-time 4D representations that preserve identity, appearance, motion, and geometry as coherent, controllable human signals.',
    tags: ['Gaussian Avatars', 'Neural Fields', 'Hybrid Representations'],
    color: '#dfff3f',
  },
  {
    no: '02',
    title: 'GENERATE',
    ko: '생성하다',
    text: 'Generative systems for human motion, appearance, expression, gaze, and behavior that remain controllable across time.',
    tags: ['Motion Generation', 'Neural Rendering', 'Behavior Synthesis'],
    color: '#8b7dff',
  },
  {
    no: '03',
    title: 'INTERACT',
    ko: '상호작용하다',
    text: 'Embodied digital humans that perceive people and environments, reason about context, and respond through coordinated action.',
    tags: ['Embodied Agents', 'Social Intelligence', 'Real-time Control'],
    color: '#ff704d',
  },
]

const focusAreas = [
  ['4D', 'HUMAN REPRESENTATION'],
  ['RT', 'REAL-TIME INTERACTION'],
  ['GEN', 'MOTION + APPEARANCE'],
  ['EMB', 'EMBODIED INTELLIGENCE'],
]

function HumanFigure({ playing }) {
  return (
    <div
      className={`figure-wrap ${playing ? 'playing' : ''}`}
      aria-label="Animated conceptual visualization of a digital human"
    >
      <div className="scan-ring ring-a" />
      <div className="scan-ring ring-b" />
      <div className="ground-ring" />
      <div className="human">
        <div className="head"><i /><i /><i /></div>
        <div className="neck" />
        <div className="torso"><span /><span /><span /></div>
        <div className="arm left"><span /><span /></div>
        <div className="arm right"><span /><span /></div>
        <div className="leg left"><span /><span /></div>
        <div className="leg right"><span /><span /></div>
      </div>
      <div className="point-field">
        {Array.from({ length: 42 }, (_, i) => (
          <i
            key={i}
            style={{
              '--x': `${(i * 47) % 100}%`,
              '--y': `${(i * 73) % 100}%`,
              '--d': `${(i % 7) * -0.3}s`,
            }}
          />
        ))}
      </div>
      <div className="axis-label label-a">GAZE VECTOR <b>ACTIVE</b></div>
      <div className="axis-label label-b">SKELETON <b>TRACKING</b></div>
    </div>
  )
}

export default function App() {
  const [playing, setPlaying] = useState(true)
  const [menu, setMenu] = useState(false)
  const [active, setActive] = useState(0)
  const [time, setTime] = useState('00:00:00')

  useEffect(() => {
    const started = Date.now()
    const id = setInterval(() => {
      const sec = Math.floor((Date.now() - started) / 1000)
      setTime(
        `00:${String(Math.floor(sec / 60)).padStart(2, '0')}:${String(sec % 60).padStart(2, '0')}`,
      )
    }, 1000)
    return () => clearInterval(id)
  }, [])

  return (
    <main>
      <nav>
        <a className="brand" href="#top">
          <span>4D</span>
          INTERACTIVE DIGITAL HUMANS
          <small>4D HUMAN INTELLIGENCE</small>
        </a>
        <div className={`navlinks ${menu ? 'open' : ''}`}>
          <a href="#research" onClick={() => setMenu(false)}>RESEARCH</a>
          <a href="#framework" onClick={() => setMenu(false)}>FRAMEWORK</a>
          <a href="#manifesto" onClick={() => setMenu(false)}>QUESTION</a>
          <button
            className="access"
            onClick={() => document.getElementById('research').scrollIntoView({ behavior: 'smooth' })}
          >
            EXPLORE RESEARCH <ArrowUpRight size={15} />
          </button>
        </div>
        <button className="menu" onClick={() => setMenu(!menu)} aria-label="Toggle navigation">
          {menu ? <X /> : <Menu />}
        </button>
      </nav>

      <section className="hero" id="top">
        <div className="hero-grid" />
        <div className="side-code">INTERACTIVE DIGITAL HUMANS / RESEARCH 2026</div>
        <div className="eyebrow"><span className="pulse" /> RESEARCH INITIATIVE · 2026</div>
        <h1>
          BUILDING<br />
          <em>HUMANS</em><br />
          BEYOND<br />
          <strong>FRAMES.</strong>
        </h1>
        <p className="lede">
          AI-driven digital humans that can be <b>represented, generated, controlled,</b> and <b>embodied</b> in real time for natural interaction with people and virtual environments.
        </p>
        <a href="#research" className="scroll"><ArrowDown size={15} /> EXPLORE THE RESEARCH</a>

        <div className="visual-panel">
          <HumanFigure playing={playing} />
          <div className="panel-top">
            <span><CircleDot size={12} /> CONCEPT SIMULATION</span>
            <b>{time}</b>
          </div>
          <button
            className="play"
            onClick={() => setPlaying(!playing)}
            aria-label={playing ? 'Pause simulation' : 'Play simulation'}
          >
            {playing ? <Pause size={17} /> : <Play size={17} />}
          </button>
          <div className="panel-bottom">
            <span>TRACK <b>REPRESENT</b></span>
            <span>TRACK <b>GENERATE</b></span>
            <span>TRACK <b>INTERACT</b></span>
          </div>
        </div>
      </section>

      <section className="statement" id="manifesto">
        <div className="kicker">THE RESEARCH QUESTION</div>
        <h2>HOW DO WE GIVE<br />DIGITAL HUMANS<br /><em>A SENSE OF NOW?</em></h2>
        <p>
          How can AI-driven digital humans be represented, generated, and embodied in real time for natural interaction with humans and virtual environments?
        </p>
      </section>

      <section className="pillars" id="research">
        <div className="section-head">
          <div>
            <span>RESEARCH PILLARS</span>
            <h2>FROM REPRESENTATION<br />TO <em>PRESENCE.</em></h2>
          </div>
          <p>
            Three interconnected research tracks connect graphics, machine learning, human motion, and embodied interaction.
          </p>
        </div>

        <div className="pillar-list">
          {pillars.map((pillar, index) => (
            <article
              key={pillar.no}
              className={active === index ? 'active' : ''}
              onMouseEnter={() => setActive(index)}
              style={{ '--accent': pillar.color }}
            >
              <header><span>{pillar.no}</span><Network size={24} /></header>
              <div className="orb"><span /></div>
              <h3>{pillar.title}<small>{pillar.ko}</small></h3>
              <p>{pillar.text}</p>
              <div className="tags">{pillar.tags.map((tag) => <span key={tag}>{tag}</span>)}</div>
              <button onClick={() => setActive(index)}>EXPLORE TRACK <ChevronRight size={15} /></button>
            </article>
          ))}
        </div>
      </section>

      <section className="framework" id="framework">
        <div className="framework-copy">
          <span className="green-label"><Sparkles size={14} /> INTERACTIVE 4D FRAMEWORK</span>
          <h2>ONE HUMAN.<br />EVERY <em>DIMENSION.</em></h2>
          <p>
            The long-term goal is to close the loop between perception and action while maintaining identity, physical plausibility, temporal continuity, and social context.
          </p>
          <a href="#pipeline">VIEW RESEARCH FRAMEWORK <ArrowUpRight size={15} /></a>
        </div>

        <div className="pipeline" id="pipeline">
          <div className="flow-line" />
          {['PERCEIVE', 'UNDERSTAND', 'GENERATE', 'ACT'].map((label, index) => (
            <div className="flow" key={label}>
              <span>0{index + 1}</span>
              <div>
                <i>
                  {index === 0 ? <Radio /> : index === 1 ? <CircleDot /> : index === 2 ? <Sparkles /> : <Network />}
                </i>
              </div>
              <b>{label}</b>
              <small>{['Multi-modal sensing', 'World + social context', 'Motion + appearance', 'Real-time embodiment'][index]}</small>
            </div>
          ))}
        </div>
      </section>

      <section className="numbers" aria-label="Research focus areas">
        <div className="number-intro">
          <span>RESEARCHING<br />THE STACK OF<br /><em>PRESENCE.</em></span>
        </div>
        {focusAreas.map(([value, label]) => (
          <div className="metric" key={label}>
            <strong>{value}</strong>
            <span>{label}</span>
          </div>
        ))}
      </section>

      <footer>
        <a className="brand" href="#top"><span>4D</span>INTERACTIVE DIGITAL HUMANS</a>
        <p>REAL-TIME 4D REPRESENTATION, GENERATION,<br />CONTROL, AND EMBODIED INTERACTION.</p>
        <div>
          <a href="https://github.com/reusahn" target="_blank" rel="noreferrer">GITHUB / REUSAHN</a>
          <span>JONGHOON AHN · 2026</span>
        </div>
      </footer>
    </main>
  )
}
