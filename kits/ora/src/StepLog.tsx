export type StepState = 'done' | 'running' | 'failed';

export interface Step {
  text: string;
  state: StepState;
}

export interface StepLogProps {
  steps: Step[];
  className?: string;
}

const MARK: Record<StepState, string> = { done: '✓', running: '', failed: '×' };

/**
 * The pack's loading idiom. One mono line per step, appended as it happens, the
 * running line carrying the caret. Nothing slides: a run appends a line every
 * few hundred milliseconds and animating the append would be motion on a
 * high-repetition path.
 */
export function StepLog({ steps, className }: StepLogProps) {
  return (
    <ul className={['ora-steplog', className].filter(Boolean).join(' ')}>
      {steps.map((step, i) => (
        <li
          key={`${i}-${step.text}`}
          className={['ora-steplog__row', `ora-steplog__row--${step.state}`].join(' ')}
        >
          <span className="ora-steplog__dot" aria-hidden="true" />
          <span className="ora-steplog__mark" aria-hidden="true">
            {MARK[step.state]}
          </span>
          <span className="ora-steplog__text">{step.text}</span>
          {step.state === 'running' && <span className="ora-steplog__caret" aria-hidden="true" />}
        </li>
      ))}
    </ul>
  );
}
