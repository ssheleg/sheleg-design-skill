import type { ReactNode } from 'react';

export interface TerminalTab {
  id: string;
  label: string;
  command: string;
}

export interface TerminalProps {
  tabs: TerminalTab[];
  /** Which tab's command is showing. The component is presentational. */
  activeId?: string;
  onSelect?: (id: string) => void;
  /** The prompt glyph. `$` in the reference. */
  prompt?: string;
  /** A copy affordance that reports in place, never a toast. */
  action?: ReactNode;
  className?: string;
}

export function Terminal({
  tabs,
  activeId,
  onSelect,
  prompt = '$',
  action,
  className,
}: TerminalProps) {
  const active = tabs.find((t) => t.id === activeId) ?? tabs[0];
  return (
    <div className={['pc-term', className].filter(Boolean).join(' ')}>
      <div className="pc-term__head">
        <span className="pc-term__dots" aria-hidden="true">
          <i />
          <i />
          <i />
        </span>
        <div className="pc-term__tabs" role="tablist">
          {tabs.map((t) => (
            <button
              key={t.id}
              type="button"
              role="tab"
              aria-selected={t.id === active?.id}
              className={[
                'pc-term__tab',
                t.id === active?.id ? 'pc-term__tab--active' : undefined,
              ]
                .filter(Boolean)
                .join(' ')}
              onClick={() => onSelect?.(t.id)}
            >
              {t.label}
            </button>
          ))}
        </div>
      </div>
      <div className="pc-term__body">
        <span className="pc-term__prompt" aria-hidden="true">
          {prompt}
        </span>
        <code className="pc-term__cmd">{active?.command}</code>
        {action}
      </div>
    </div>
  );
}
