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

const baselineMetrics = [
  ['36', 'SAVED PROBE RUNS'],
  ['472,958', 'HUMAN GAUSSIANS'],
  ['26.6%', 'ANKLE Z LEAKAGE'],
  ['11.2%', 'WRIST Z LEAKAGE'],
]

const heatmapUrl = 'https://raw.githubusercontent.com/reusahn/interactive-digital-humans/main/experiments/01-baseline/figures/01_joint_axis_leakage.svg'
const confidenceUrl = 'https://raw.githubusercontent.com/reusahn/interactive-digital-humans/main/experiments/01-baseline/figures/02_high_confidence_leakage.svg'
const resultsUrl = 'https://github.com/reusahn/interactive-digital-humans/blob/main/experiments/01-baseline/results.md'
const dataManifestUrl = 'https://github.com/reusahn/interactive-digital-humans/blob/main/experiments/01-baseline/DATA_MANIFEST.md'

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
      <style>{`
        .baseline{padding:120px 6vw 130px;background:#0d100e;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
        .baseline-head{display:grid;grid-template-columns:1.35fr .8fr;gap:70px;align-items:end;margin-bottom:52px}
        .baseline-kicker{font:500 9px DM Mono;letter-spacing:.15em;color:var(--lime);margin-bottom:16px}
        .baseline h2{font:600 clamp(42px,5.4vw,74px)/.96 Space Grotesk;letter-spacing:-.055em;margin:0}
        .baseline h2 em{font-style:normal;color:transparent;-webkit-text-stroke:1px #717771}
        .baseline-head>p{font:12px/1.8 DM Mono;color:#858b84;margin:0}
        .baseline-head>p b{color:#f1f3ee}
        .baseline-stats{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid #2a302a;margin-bottom:36px}
        .baseline-stat{padding:26px 22px;border-right:1px solid #2a302a;min-height:118px;display:flex;flex-direction:column;justify-content:space-between}
        .baseline-stat:last-child{border-right:0}.baseline-stat strong{font:600 clamp(26px,3vw,43px) Space Grotesk;color:#f1f4ed;letter-spacing:-.045em}.baseline-stat span{font:8px DM Mono;letter-spacing:.12em;color:#737a72}
        .baseline-figures{display:grid;grid-template-columns:1.25fr .75fr;gap:18px}
        .baseline-figure{border:1px solid #2b312b;background:#111411;padding:16px;min-width:0}
        .baseline-figure img{width:100%;height:auto;display:block;background:white}
        .baseline-figure figcaption{padding:15px 4px 2px;font:9px/1.6 DM Mono;color:#747b73;letter-spacing:.03em}
        .baseline-figure figcaption b{color:#dfe4dc;font-weight:500}
        .baseline-insight{margin-top:18px;border:1px solid #2b312b;display:grid;grid-template-columns:1.2fr .8fr}
        .baseline-question{padding:34px}.baseline-question span{font:8px DM Mono;letter-spacing:.15em;color:var(--lime)}
        .baseline-question p{font:500 clamp(20px,2.4vw,31px)/1.32 Space Grotesk;letter-spacing:-.025em;margin:16px 0 0;color:#e9ede6}
        .baseline-notes{padding:34px;border-left:1px solid #2b312b;font:11px/1.75 Inter;color:#838a82}.baseline-notes b{color:#e8ece5}.baseline-notes p{margin:0 0 15px}
        .baseline-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}.baseline-actions a{display:inline-flex;align-items:center;gap:9px;border:1px solid #3a4239;padding:11px 13px;font:500 8px DM Mono;letter-spacing:.1em;color:#bdc4ba}.baseline-actions a:first-child{border-color:var(--lime);color:var(--lime)}
        @media(max-width:900px){.baseline{padding:85px 25px}.baseline-head,.baseline-figures,.baseline-insight{grid-template-columns:1fr}.baseline-stats{grid-template-columns:1fr 1fr}.baseline-stat:nth-child(2){border-right:0}.baseline-stat{border-bottom:1px solid #2a302a}.baseline-notes{border-left:0;border-top:1px solid #2b312b}.baseline-head{gap:25px}}
        @media(max-width:540px){.baseline-stats{grid-template-columns:1fr}.baseline-stat{border-right:0}.baseline-figure{padding:8px}}
      `}</style>

      <nav>
        <a className="brand" href="#top">
          <span>4D</span>
          INTERACTIVE DIGITAL HUMANS
          <small>4D HUMAN INTELLIGENCE</small>
        </a>
        <div className={`navlinks ${menu ? 'open' : ''}`}>
          <a href="#research" onClick={() => setMenu(false)}>RESEARCH</a>
          <a href="#baseline" onClick={() => setMenu(false)}>BASELINE 01</a>
          <a href="#framework" onClick={() => setMenu(false)}>FRAMEWORK</a>
          <a href="#manifesto" onClick={() => setMenu(false)}>QUESTION</a>
          <button
            className="access"
            onClick={() => document.getElementById('baseline').scrollIntoView({ behavior: 'smooth' })}
          >
            VIEW RESULTS <ArrowUpRight size={15} />
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

      <section className="baseline" id="baseline">
        <div className="baseline-head">
          <div>
            <div className="baseline-kicker">BASELINE 01 · HUGS / HUMAN GAUSSIAN SPLATS</div>
            <h2>WHERE DOES<br />DEFORMATION <em>LEAK?</em></h2>
          </div>
          <p>
            A controlled deformation-locality probe on the pretrained NeuMan <b>Seattle</b> sequence. Small SMPL joint rotations are used to measure how much Gaussian motion remains inside an expected kinematic subtree and how much propagates outside it.
          </p>
        </div>

        <div className="baseline-stats">
          {baselineMetrics.map(([value, label]) => (
            <div className="baseline-stat" key={label}>
              <strong>{value}</strong>
              <span>{label}</span>
            </div>
          ))}
        </div>

        <div className="baseline-figures">
          <figure className="baseline-figure">
            <img src={heatmapUrl} alt="HuGS deformation leakage heatmap by joint and rotation axis" />
            <figcaption><b>FIG. 01</b> · Joint × axis leakage at ±10°, sign-averaged. Distal ankle and wrist articulations show substantially higher apparent non-target displacement than the shoulder in Seattle frame 0.</figcaption>
          </figure>
          <figure className="baseline-figure">
            <img src={confidenceUrl} alt="HuGS deformation leakage after high-confidence joint assignment filtering" />
            <figcaption><b>FIG. 02</b> · The principal distal-versus-proximal pattern remains visible after retaining only Gaussians with joint-assignment confidence ≥ 0.9.</figcaption>
          </figure>
        </div>

        <div className="baseline-insight">
          <div className="baseline-question">
            <span>CURRENT RESEARCH QUESTION</span>
            <p>Why do distal articulations produce greater non-local Gaussian deformation, and can control be made more anatomically local without sacrificing rendering or animation quality?</p>
          </div>
          <div className="baseline-notes">
            <p><b>Wrist behavior.</b> The z-axis wrist sweep is approximately sign-symmetric and magnitude-linear from ±5° to ±30°, while the leakage proportion stays near 11.21%.</p>
            <p><b>Scope.</b> These are Baseline v1 observations from one NeuMan sequence and one validation frame. They are not yet a general claim about HUGS.</p>
            <p><b>Data policy.</b> Large per-Gaussian NPZ arrays remain in Google Drive as the authoritative raw archive. Compact tables, figures, code, and provenance are versioned on GitHub.</p>
            <div className="baseline-actions">
              <a href={resultsUrl} target="_blank" rel="noreferrer">FULL RESULTS <ArrowUpRight size={13} /></a>
              <a href={dataManifestUrl} target="_blank" rel="noreferrer">DATA MANIFEST <ArrowUpRight size={13} /></a>
            </div>
          </div>
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
          <a href="https://github.com/reusahn/interactive-digital-humans" target="_blank" rel="noreferrer">GITHUB / RESEARCH REPOSITORY</a>
          <span>JONGHOON AHN · 2026</span>
        </div>
      </footer>
    </main>
  )
}
